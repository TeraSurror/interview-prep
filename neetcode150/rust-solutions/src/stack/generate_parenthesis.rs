fn generate_parenthesis(m: i32) -> Vec<String> {
    let mut res: Vec<String> = vec![];

    fn backtrack(res: &mut Vec<String>, s: String, open: i32, close: i32) {
        if open == 0 && close == 0 {
            res.push(s);
            return;
        }

        if open == close {
            backtrack(res, s.clone() + "(", open - 1, close);
        } else {
            if open > 0 {
                backtrack(res, s.clone() + "(", open - 1, close);
            } 
            if close > 0 {
                backtrack(res, s.clone() + ")", open, close - 1);
            }
        }
    }

    backtrack(&mut res, String::from(""), m, m);
    res
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_generate_parenthesis_1() {
        let m = 1;
        let got = generate_parenthesis(m);
        let want = vec![String::from("()")];
        assert_eq!(want, got);
    }

    #[test]
    fn test_generate_parenthesis_2() {
        let m = 3;
        let got = generate_parenthesis(m);
        let want = vec![
            String::from("((()))"),
            String::from("(()())"),
            String::from("(())()"),
            String::from("()(())"),
            String::from("()()()"),
        ];
        assert_eq!(want, got);
    }
}
