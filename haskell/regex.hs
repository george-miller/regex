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
  show = nodeString 0

instance Show Graph where
  show g = graphString g

simpleNodeString :: Node -> String
simpleNodeString n = "Node matches " ++ [matches n]
nodeString :: Int -> Node -> String
nodeString numIndent n
  | edges n == [] = thisNodeString
  | otherwise = thisNodeString ++ nextNodeStrings 
  where
      createIndent numIndent = concat $ replicate numIndent "\t"
      thisNodeString = createIndent numIndent ++ simpleNodeString n ++ "\n"
      nextNodeStrings = concat $ map (nodeString $ numIndent+1) (edges n)

graphString :: Graph -> String
graphString g = intercalate "\n" $ map (nodeString 0) (inputNodes g)

a, b, c :: Node
f = Node 'f' []
d = Node 'd' []
c = Node 'c' [Node 'e' [f]]
b = Node 'b' [d]
a = Node 'a' [b, c]
z = Node 'z' []

g :: Graph
g = Graph [a, z] [d, f, z]
