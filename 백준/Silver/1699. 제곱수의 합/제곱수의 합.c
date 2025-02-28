int dp[100001] = { 0, };  // dp 배열 초기화

int main(void) {
    int n;
    scanf("%d", &n);

    // dp 배열 초기화
    for (int i = 1; i <= n; i++) {
        dp[i] = 100001;  // 최대값으로 초기화 (최소 개수를 찾으므로)
    }

    dp[0] = 0;  // 0을 제곱수들의 합으로 표현할 때는 0개 항 필요

    // 동적 계획법으로 dp 배열 채우기
    for (int i = 1; i <= n; i++) {
        for (int j = 1; j * j <= i; j++) {
            dp[i] = (dp[i] < dp[i - j * j] + 1) ? dp[i] : dp[i - j * j] + 1;
        }
    }

    // 결과 출력
    printf("%d", dp[n]);
    return 0;
}