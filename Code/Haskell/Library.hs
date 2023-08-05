module Library where
import PdePreludat

fibonacci :: Number -> [Number]
fibonacci n
    | n <= 0 = []
    | n == 1 = [0]
    | n == 2 = [0, 1]
    | otherwise = fibonacci' [0, 1] (n - 2)
    where fibonacci' xs count
            | count <= 0 = xs
            | otherwise = fibonacci' (xs ++ [sum $ drop (length xs - 2) xs]) (count - 1)


bubbleSort :: Ord a => [a] -> [a]
bubbleSort [] = []
bubbleSort xs = bubbleSort (init sorted) ++ [last sorted]
    where sorted = foldr bubble [] xs
          bubble x [] = [x]
          bubble x (y:ys)
              | x <= y = x:y:ys
              | otherwise = y : bubble x ys