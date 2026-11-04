SELECT DISTINCT U.name, 
IFNULL(SUM(R.distance) OVER (PARTITION BY U.id),0) as travelled_distance
FROM Users as U
LEFT JOIN Rides as R
ON U.id = R.user_id
ORDER BY travelled_distance desc , name