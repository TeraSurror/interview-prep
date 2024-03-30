use std::{cmp::max, collections::VecDeque};

fn length_of_longest_substring(s: String) -> i32 {
    let mut q = VecDeque::new();
    let mut result = 0;

    for c in s.chars() {
        while q.contains(&c) {
            q.pop_front();
        }
        q.push_back(c);
        result = max(result, q.len());
    }

    return result as i32;
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_longest_substring() {
        let s = String::from("asjfaklsf");
        let got = length_of_longest_substring(s);
        let want = 6;
        assert_eq!(want, got);
    }
}
