CREATE TABLE finals AS
  SELECT "RSF" AS hall, "61A" as course UNION
  SELECT "Wheeler"    , "61A"           UNION
  SELECT "Pimentel"   , "61A"           UNION
  SELECT "Li Ka Shing", "61A"           UNION
  SELECT "Stanley"    , "61A"           UNION
  SELECT "RSF"        , "61B"           UNION
  SELECT "Wheeler"    , "61B"           UNION
  SELECT "Morgan"     , "61B"           UNION
  SELECT "Wheeler"    , "61C"           UNION
  SELECT "Pimentel"   , "61C"           UNION
  SELECT "Soda 310"   , "61C"           UNION
  SELECT "Soda 306"   , "10"            UNION
  SELECT "RSF"        , "70";

CREATE TABLE sizes AS
  SELECT "RSF" AS room, 900 as seats    UNION
  SELECT "Wheeler"    , 700             UNION
  SELECT "Pimentel"   , 500             UNION
  SELECT "Li Ka Shing", 300             UNION
  SELECT "Stanley"    , 300             UNION
  SELECT "Morgan"     , 100             UNION
  SELECT "Soda 306"   , 80              UNION
  SELECT "Soda 310"   , 40              UNION
  SELECT "Soda 320"   , 30;

--创建一个名为 big 的表，该表包含一个名为 course 的列（字符串类型），用于存储期末考试座位数至少为1000的课程名称（每行一个课程）。
SELECT course FROM finals,sizes WHERE hall=room GROUP BY course HAVING SUM(seats)>=1000

--创建一个名为 remaining 的表，其中包含两列，course（字符串）和 remaining（数字），每门课程对应一行。
-- 每行包含课程的名称，以及该课程所有期末考场座位总数，扣除座位数最多的考场后的剩余座位数。
SELECT course,SUM(seats)-MAX(seats) AS remaining FROM finals,sizes WHERE hall=room GROUP BY course

--创建一个名为 sharing 的表，其中包含两列，course（字符串）和 shared（数字），每门课程使用至少一个也被其他课程使用的教室对应一行。
-- 每行包含课程的名称，以及该课程与其他课程共享的教室总数。
--提醒：COUNT(DISTINCT x) 用于计算每个分组中列 x 的不同值的数量。
CREATE TABLE sharing AS
 SELECT course,COUNT(DISTINCT hall) AS shared FROM finals as a,finals as b 
 WHERE a.hall=b.hall AND a.course<>b.course GROUP BY a.course HAVING COUNT(DISTINCT hall)>0