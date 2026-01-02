CREATE TABLE parents AS
  SELECT "abraham" AS parent, "barack" AS child UNION
  SELECT "abraham"          , "clinton"         UNION
  SELECT "delano"           , "herbert"         UNION
  SELECT "fillmore"         , "abraham"         UNION
  SELECT "fillmore"         , "delano"          UNION
  SELECT "fillmore"         , "grover"          UNION
  SELECT "eisenhower"       , "fillmore";

CREATE TABLE dogs AS
  SELECT "abraham" AS name, "long" AS fur, 26 AS height UNION
  SELECT "barack"         , "short"      , 52           UNION
  SELECT "clinton"        , "long"       , 47           UNION
  SELECT "delano"         , "long"       , 46           UNION
  SELECT "eisenhower"     , "short"      , 35           UNION
  SELECT "fillmore"       , "curly"      , 32           UNION
  SELECT "grover"         , "short"      , 28           UNION
  SELECT "herbert"        , "curly"      , 31;

CREATE TABLE sizes AS
  SELECT "toy" AS size, 24 AS min, 28 AS max UNION
  SELECT "mini"       , 28       , 35        UNION
  SELECT "medium"     , 35       , 45        UNION
  SELECT "standard"   , 45       , 60;

-- 所有有父母的狗，按父母身高从高到低排列
CREATE TABLE by_parent_height AS
  SELECT child FROM parents WHERE parent=name ORDER BY height ;

-- 每只狗的尺寸
CREATE TABLE size_of_dogs AS
  SELECT name,size FROM dogs,sizes WHERE min<=height AND max>=height;

--有两对兄弟姐妹的尺寸相同。
--创建一个表，其中包含一行字符串，对应于每对兄弟姐妹。
--每个字符串都应该是一个描述这些尺寸相同的兄弟姐妹的句子。

-- 填写这个辅助表是可选的
CREATE TABLE siblings AS
  SELECT a.child AS first,b.child AS second FROM parents as a,parents as b WHERE a.parent=b.parent and a.child>b.child 

-- 关于尺寸相同的兄弟姐妹的句子
CREATE TABLE sentences AS
  SELECT "The two sibilings" || first || "and" || second || "has the same size:" ||size
  FROM siblings,size_of_dogs as a,size_of_dogs as b WHERE first=a.name AND second=b.name AND a.size=b.size

-- 记录所有身高与平均身高差异不超过30%的毛发类型，并计算其身高范围
CREATE TABLE low_variance AS
  SELECT fur,MAX(height)-MIN(height) FROM dogs GROUP BY fur HAVING MAX(height)<=1.3*AVE(height) AND MIN(height)>=0.7*AVE(height);

-- 示例：
SELECT * FROM low_variance;
-- 预期输出：
-- curly|1
--补充：有两只卷毛狗：fillmore 身高 32，herbert 身高 31。这给出的身高范围为 1。