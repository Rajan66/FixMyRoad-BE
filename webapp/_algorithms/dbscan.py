def dbscan(points, eps=200, min_samples=2, distance_func=None):
    """
    points: list of (id, lat, lon)
    eps: max distance in meters
    min_samples: minimum number of neighbors to form a core point
    distance_func: function(lat1, lon1, lat2, lon2)
    Returns: dict of point_id -> cluster_id (or -1 for noise)
    """
    cluster_id = 0
    visited = set()
    clusters = {}
    noise = set()

    point_map = {pid: (lat, lon) for pid, lat, lon in points}

    def region_query(pid):
        lat1, lon1 = point_map[pid]
        return [
            other_id
            for other_id, (lat2, lon2) in point_map.items()
            if distance_func(lat1, lon1, lat2, lon2) <= eps
        ]

    def expand_cluster(pid, neighbors, cid):
        clusters[pid] = cid
        i = 0
        while i < len(neighbors):
            neighbor = neighbors[i]
            if neighbor not in visited:
                visited.add(neighbor)
                neighbor_neighbors = region_query(neighbor)
                if len(neighbor_neighbors) >= min_samples:
                    neighbors.extend(
                        [n for n in neighbor_neighbors if n not in neighbors]
                    )
            if neighbor not in clusters:
                clusters[neighbor] = cid
            i += 1

    for pid, _, _ in points:
        if pid in visited:
            continue
        visited.add(pid)
        neighbors = region_query(pid)
        if len(neighbors) >= min_samples:
            expand_cluster(pid, neighbors, cluster_id)
            cluster_id += 1
        else:
            noise.add(pid)

    for nid in noise:
        clusters[nid] = -1

    return clusters
