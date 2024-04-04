use std::collections::VecDeque;

fn perform_operation(num1: i32, num2: i32, operation: String) -> i32 {
    if operation == String::from("+") {
        num1 + num2
    } else if operation == String::from("-") {
        num1 - num2        
    } else if operation == String::from("*") {
        num1 * num2
    } else {
        num1 / num2
    }
}

fn eval_rpn(tokens: Vec<String>) -> i32 {
    let mut stack = VecDeque::new();

    for token in tokens {
        if token.parse::<i32>().is_ok() {
            stack.push_back(token.parse::<i32>().unwrap())
        } else {
            let num2 = stack.pop_back().unwrap();
            let num1 = stack.pop_back().unwrap();
            let res = perform_operation(num1, num2, token);
            stack.push_back(res);
        }
    }

    stack.pop_back().unwrap()
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_polish_notation() {
        let tokens = vec!["2", "1", "+", "3", "*"];
        let tokens: Vec<String> = tokens.into_iter().map(|token| String::from(token)).collect();
        let want = 9;
        let got = eval_rpn(tokens);
        assert_eq!(want, got);
    }

    #[test]
    fn test_polish_notation_1() {
        let tokens = vec!["4", "13", "5", "/", "+"];
        let tokens: Vec<String> = tokens.into_iter().map(|token| String::from(token)).collect();
        let want = 6;
        let got = eval_rpn(tokens);
        assert_eq!(want, got);
    }

    #[test]
    fn test_polish_notation_2() {
        let tokens = vec!["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"];
        let tokens: Vec<String> = tokens.into_iter().map(|token| String::from(token)).collect();
        let want = 22;
        let got = eval_rpn(tokens);
        assert_eq!(want, got);
    }
}
