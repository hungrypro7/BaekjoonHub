#include <iostream>
#include <vector>
#include <queue>
#include <limits.h>

using namespace std;

int n, m; // 헛간의 수, 소들의 길 개수
vector<vector<pair<int, int>>> maps; // 인접 리스트
vector<int> dis; // 거리 저장 배열

void dijkstra(int start) {
    priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> pq; // 최소 힙 사용
    pq.push({0, start});
    dis[start] = 0;

    while (!pq.empty()) {
        int d = pq.top().first;  // 현재 거리
        int now = pq.top().second; // 현재 위치
        pq.pop();

        if (dis[now] < d) continue; // 현재 거리가 더 크면 패스

        for (auto &edge : maps[now]) {
            int v = edge.first; // 다음 노드
            int w = edge.second; // 가중치
            int cost = d + w;

            if (cost < dis[v]) {
                dis[v] = cost;
                pq.push({cost, v});
            }
        }
    }
}

int main() {
    cin >> n >> m;
    maps.resize(n + 1);
    dis.resize(n + 1, INT_MAX);

    for (int i = 0; i < m; i++) {
        int a, b, c;
        cin >> a >> b >> c;
        maps[a].push_back({b, c});
        maps[b].push_back({a, c});
    }

    dijkstra(1); // 시작점 1에서 다익스트라 실행
    cout << dis[n] << endl; // 1번 헛간에서 n번 헛간까지의 최단 거리 출력

    return 0;
}