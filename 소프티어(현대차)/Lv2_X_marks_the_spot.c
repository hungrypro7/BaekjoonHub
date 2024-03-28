int main() {
    int n;
    scanf("%d", &n);
    getchar(); // 버퍼에 남은 개행 문자 제거

    for (int i = 0; i < n; i++) {
        char s[500001], t[500001]; // 가정: s와 t의 최대 길이는 100
        scanf("%s %s", s, t);
        getchar(); // 버퍼에 남은 개행 문자 제거

        for (int idx = 0; idx < strlen(s); idx++) {
            if (s[idx] == 'x' || s[idx] == 'X') {
                if (islower(t[idx])) { // 소문자일 때
                    printf("%c", toupper(t[idx]));
                } else {
                    printf("%c", t[idx]);
                }
                break; // 첫 번째 'x' 또는 'X'를 만났을 때 출력 후 루프 종료
            }
        }
    }
    printf("\n"); // 모든 출력이 끝난 후 개행
    return 0;
}
