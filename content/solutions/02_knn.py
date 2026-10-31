knn_degrees = Graph.build_knn(df.centroid.to_crs(4326), k=8)

changed = [i for i in df.index if set(knn[i].index) != set(knn_degrees[i].index)]
print(f"{len(changed)} tracts ({len(changed) / knn.n:.0%}) get a different neighbor set from coordinates in degrees")
