import Test.HUnit (Test(TestCase))
import Input (echo)
import HUnitJudge (isEqual, runJSON)

echo' = echo :: [Int] -> [Int]

empty = []

main = runJSON
    [ TestCase (isEqual "echo [1,2,3]" [1,2,3]  (echo' [1,2,3]))
    , TestCase (isEqual "echo []"      empty    (echo' empty))
    , TestCase (isEqual "echo [1]"     [1]      (echo' [1]))
    , TestCase (isEqual "echo [1,1]"   [1,1]    (echo' [1,1]))
    ]
