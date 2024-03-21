fn length_of_longest_substring(s: String) -> i32 {
    return 0;
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_longest_substring() {
        let s = String::from("asjfaklsf");
        let got = length_of_longest_substring(s);
        let want = 7;
        assert_eq!(want, got);
    }
}
