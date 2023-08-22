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
    where fibonacci' cola conteo
            | conteo <= 0 = cola
            | otherwise = fibonacci' (cola ++ [sum $ drop (length cola - 2) cola]) (conteo - 1)

{-Función bubbleSort-}
bubbleSort :: Ord a => [a] -> [a]
--Caso base
bubbleSort [] = []
--Caso recursivo
bubbleSort cola = bubbleSort (init ordenado) ++ [last ordenado]
    where ordenado = foldr bubble [] cola
          bubble x [] = [x]
          bubble x (y:ys)
              | x <= y = x:y:ys
              | otherwise = y : bubble x ys

{-Aclaración-}
--En Haskell para evaluar el tiempo de ejecución y memoria tenemos el comando de consola:
--ghci> :set +s
--Se ejecuta tal comando antes de ejecutar el resto de las funciones en cuestión.