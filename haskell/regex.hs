module Regex where
import Data.List
data Node = Node { matches :: Char,
                   edges :: [Node]
                 }
data Graph = Graph { inputNodes :: [Node],
                     outputNodes :: [Node]
                   }

instance Eq Node where
  n1 == n2 = matches n1 == matches n2

instance Show Node where
  show = nodeString 1

instance Show Graph where
  show g = graphString g

simpleNodeString :: Node -> String
simpleNodeString n = "Node matches " ++ [matches n]
nodeString :: Int -> Node -> String
nodeString numIndent n
  | edges n == [] = simpleNodeString n
  | otherwise = intercalate (concat $ "\n":(replicate numIndent "\t")) $ simpleNodeString n:map (nodeString (numIndent+1)) (edges n)

graphString :: Graph -> String
graphString g = intercalate "\n" $ map (nodeString 1) (inputNodes g)

a, b, c :: Node
f = Node 'f' []
d = Node 'd' []
c = Node 'c' [Node 'e' [f]]
b = Node 'b' [d]
a = Node 'a' [b, c]
z = Node 'z' []

g :: Graph
g = Graph [a, z] [d, f, z]
