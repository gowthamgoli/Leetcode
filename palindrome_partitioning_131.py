def partition(s):
    def dfs(output, s, path, level=0):
        if len(s) == 0:
            output.append(path)

        for i in range(1, len(s) + 1):
            if s[:i] != s[:i][::-1]: continue
            print('|' + '\u2014' * 4 * level , path + [s[:i]], s[i:])
            dfs(output, s[i:], path + [s[:i]], level=level+1 )
            

    output = []
    dfs(output, s[:], [])
    return output

if __name__ == "__main__":
    # print(partition("aab"))
    print(partition("xxxx"))