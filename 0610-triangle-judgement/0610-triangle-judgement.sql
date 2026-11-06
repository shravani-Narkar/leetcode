SELECT x,y,z, CASE WHEN (abs(x+y) > abs(z)) AND (abs(y+z) > abs(x)) AND (abs(x+z) > abs(y)) THEN 'Yes' ELSE 'No' END as triangle
FROM Triangle