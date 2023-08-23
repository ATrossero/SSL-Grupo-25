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
            | conteo <= 0 = cola --Corta recursividad y devuelve la lista como está
            | otherwise = fibonacci' (cola ++ [sum $ drop (length cola - 2) cola]) (conteo - 1)
            --Si se puede seguir: calcula el siguiente número, actualiza la lista con el nuevo
            --número calculado y llama a la función de vuelta con el conteo y lista actualizada 

{-Función bubbleSort-}
bubbleSort :: Ord a => [a] -> [a]
--Caso base
bubbleSort [] = []
--Caso recursivo
bubbleSort cola = bubbleSort (init ordenado) ++ [last ordenado]
    --Aplicamos la función bubble a la cola mediante foldr
    where ordenado = foldr bubble [] cola
    --Definiciones de la función bubble
          bubble x [] = [x] --Si está vacía agrega directamente
          bubble x (y:ys) --Dado un elemento a incrustar
              | x <= y = x:y:ys --si es menor va primero
              | otherwise = y : bubble x ys --Si va luego, se pone detrás y se vuelve a llamar a la función

{-Aclaración-}
--En Haskell para evaluar el tiempo de ejecución y memoria tenemos el comando de consola:
--ghci> :set +s
--Se ejecuta tal comando antes de ejecutar el resto de las funciones en cuestión.