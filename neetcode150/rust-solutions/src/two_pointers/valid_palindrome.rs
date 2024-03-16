fn is_palindrome(s: String) -> bool {
    let s: Vec<char> = s
        .chars()
        .filter(|c| c.is_alphanumeric())
        .map(|c| c.to_lowercase().next().unwrap())
        .collect();

    let len = s.len();

    for i in 0..(len / 2) {
        if s[i] != s[len - i - 1] {
            return false;
        }
    }

    true
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_is_palindrome() {
        let s = "A man, a plan, a canal: Panama";
        assert!(is_palindrome(s.to_string()))
    }

    #[test]
    fn test_not_palindrome() {
        let s = String::from("A random sentence that is ofc not a palindrome");
        assert!(!is_palindrome(s))
    }
}
