##### 1

knn4 = Graph.build_knn(df.centroid, k=4)
print(f"% non-zero weights, four nearest neighbors: {knn4.pct_nonzero:.3f}")
print(f"% non-zero weights, rook: {rook.pct_nonzero:.3f}")

##### 2

fewer = (rook.cardinalities < knn4.cardinalities).sum()
print(f"{fewer} tracts have fewer rook neighbors than four-nearest neighbors")

##### 3

identical = sum(set(rook[i].index) == set(queen[i].index) for i in df.index)
print(f"{identical} tracts have identical queen and rook neighbors")
