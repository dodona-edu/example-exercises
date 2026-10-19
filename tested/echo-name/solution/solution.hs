main :: IO ()
main = do
  naam <- getLine
  putStrLn ("Hallo, " ++ naam ++ "!")
