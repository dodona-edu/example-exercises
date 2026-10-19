sumOfSquares :: [Int] -> Int
sumOfSquares xs = foldr (+) 0 (map (^ 2) xs)
