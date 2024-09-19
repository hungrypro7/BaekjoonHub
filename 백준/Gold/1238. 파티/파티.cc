#include <iostream>
#include <vector>
#include <algorithm>
#include <queue>
#include <climits>

using namespace std;

int n, m, x;
vector<vector<pair<int, int>>> roads;
vector<vector<int>> result;
vector<int> ans;

vector<int> dijkstra(int start) {
    vector<int> dis(n+1, INT_MAX);
    priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> pq; // 최소 힙 사용
    pq.push({0, start});
    dis[start] = 0;

    while (!pq.empty()) {
        int d = pq.top().first;  // 현재 거리
        int now = pq.top().second; // 현재 위치
        pq.pop();

        if (dis[now] < d) continue; // 현재 거리가 더 크면 패스

        for (auto &edge : roads[now]) {
            int v = edge.first; // 다음 노드
            int w = edge.second; // 가중치
            int cost = d + w;

            if (cost < dis[v]) {
                dis[v] = cost;
                pq.push({cost, v});
            }
        }
    }
    return dis;
}

int main() {
    cin >> n >> m >> x;    // 학생 수, 도로 개수, 파티를 벌일 마을
    roads.resize(n+1);
    
    for (int i=0; i<m; i++) {
        int start, end, time;
        cin >> start >> end >> time;
        roads[start].push_back({end, time});
    }
    
    result.resize(n+1);
    for (int i=1; i<n+1; i++) {
        result[i] = dijkstra(i);
    }
    
    for (int i=1; i<n+1; i++) {
        int temp = result[i][x] + result[x][i];
        ans.push_back(temp);
    }
    
    cout << *max_element(ans.begin(), ans.end()) << endl;
    
    return 0;
}
