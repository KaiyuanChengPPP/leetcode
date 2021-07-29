var longestCommonPrefix = function(strs) {

    let a = strs.length;
    console.log(a)
    if (a == 0) {
        return [""]
    }
    if (a == 1) {
        return strs[0]
    }
    strs.sort()
    let min = Math.min.apply(Math, strs.map(function(str) { return str.length; }))
    let i = 0
    while (i < min && strs[0][i] == strs[a - 1][i]) {
        i++
    }
    pre = strs[0].substring(0, i)
    return pre


};

strs = []
pre = longestCommonPrefix(strs)
console.log(pre)