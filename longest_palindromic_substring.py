def findAllSubStrings(s: str):
        subs = []
        for i in range(len(s)):
            for j in range(i+1, len(s) + 1):
                subs.append(s[i:j])
        return subs

if __name__ == "__main__":
    subs = findAllSubStrings('berkant')
    print(subs)