import Control.Applicative (liftA2)
import Control.Monad (forM_)

collatz :: Integral a => a -> a
collatz n
    | even n    = n `div` 2
    | otherwise = 3 * n + 1

-- Apply collatz until the result is 1
collatzSequence :: Integral a => a -> [a]
collatzSequence = takeWhile (/= 1) . iterate collatz

stoppingTime :: Integral a => a -> Int
stoppingTime = length . collatzSequence

-- Print the length of the longest collatz sequence up to multiple powers of ten
main :: IO ()
main = forM_ [1..5] $ \n -> do
    let m = maximum $ map stoppingTime [1..10^n]
    putStrLn $ concat
        ["Maximum collatz sequence length up to ", show (10^n), ": ", show m]

-- Variable-free version of the above program demonstrating the supreme elegance
-- of the GHC®/Haskell™ Programming Environment
hell :: IO ()
hell=forM_ [1..5] (putStrLn
    .liftA2(++)((("Maximum"
    ++" collatz sequence"++
    " length up to ") ++) . 
    show.(10 ^))((": " ++).
    show.maximum.map(length
    .takeWhile(/=1).iterate
    (([flip div 2,(+1).(*3)
    ]!!)=<<(fromEnum.odd)))
    .enumFromTo 1 . (10^)))
