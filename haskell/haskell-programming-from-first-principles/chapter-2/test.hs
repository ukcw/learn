sayHello :: String -> IO ()
sayHello x = putStrLn ("Hello, " ++ x ++ "!" )

waxOn = x * 5
  where x = y ^ 2
        y = z + 8
        z = 7
