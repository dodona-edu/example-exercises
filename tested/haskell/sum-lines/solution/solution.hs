main :: IO ()
main = interact (\input -> show (sum (map read (lines input))) ++ "\n")
