module Library where
import PdePreludat

{-Función fibonacci-}
fibonacci :: Number -> [Number]
fibonacci n
    --Casos base
    | n <= 0 = []
    | n == 1 = [0]
    | n == 2 = [0, 1]
    --Caso recursivo
    | otherwise = fibonacci' [0, 1] (n - 2)
    where fibonacci' xs count
            | count <= 0 = xs
            | otherwise = fibonacci' (xs ++ [sum $ drop (length xs - 2) xs]) (count - 1)

{-Función bubbleSort-}
bubbleSort :: Ord a => [a] -> [a]
--Caso base
bubbleSort [] = []
--Caso recursivo
bubbleSort xs = bubbleSort (init sorted) ++ [last sorted]
    where sorted = foldr bubble [] xs
          bubble x [] = [x]
          bubble x (y:ys)
              | x <= y = x:y:ys
              | otherwise = y : bubble x ys

{-Aclaración-}
--En Haskell para evaluar el tiempo de ejecución y memoria tenemos el comando de consola:
--ghci> :set +s
--Se ejecuta tal comando antes de ejecutar el resto de las funciones en cuestión.