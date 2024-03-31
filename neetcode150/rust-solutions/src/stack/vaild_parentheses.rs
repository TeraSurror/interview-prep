use std::collections::VecDeque;

fn is_valid(s: String) -> bool {
    let mut stack: VecDeque<char> = VecDeque::new();

    for bracket in s.chars() {
        if bracket == '(' {
            stack.push_back(')');
        } else if bracket == '{' {
            stack.push_back('}');
        } else if bracket == '[' {
            stack.push_back(']');
        } else {
            if stack.len() == 0 {
                return false;
            }
            let top = stack.pop_back().unwrap();
            if top != bracket {
                return false;
            }
        }
    }

    stack.len() == 0
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_valid() {
        let s = String::from("()");
        assert!(is_valid(s))
    }

    #[test]
    fn test_valid_1() {
        let s = String::from("(){}[]");
        assert!(is_valid(s))
    }

    #[test]
    fn test_valid_2() {
        let s = String::from("(]");
        assert!(!is_valid(s))
    }
}
