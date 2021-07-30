var isValid = function(s) {
    if (s.split("(").length != s.split(")").length || s.split("[").length != s.split("]").length || s.split("{").length != s.split("}").length)
        return false
    let stack = []
    for (let i = 0; i < s.length; i++) {
        let x = s[i]

        if (x == "(" || x == "[" || x == "{") {
            stack.push(x)
            continue
        }
        if (stack.length == 0) {
            return false
        }
        let check
        switch (x) {
            case ')':
                check = stack.pop()
                if (check == '[' || check == '{')
                    return false
                break
            case ']':
                check = stack.pop()
                if (check == '(' || check == '{')
                    return false
                break
            case '}':
                check = stack.pop()
                if (check == '(' || check == '[')
                    return false
                break
        }

    }
    return true


};

str = "([)"
let a = isValid(str)
console.log(a)