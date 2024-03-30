fn check_inclusion(s1: String, s2: String) -> bool {
    if s1.len() > s2.len() {
        return false;
    }

    let mut s1_letters = [0; 26];

    for letter in s1.chars() {
        s1_letters[letter as usize - 'a' as usize] += 1;
    }

    let s2: Vec<char> = s2.chars().collect();

    let mut start = 0;
    let mut end = s1.len();

    while end < s2.len() {
        let substring = &s2[start..end]; 
        let mut substring_letters = [0; 26];
        for letter in substring {
           substring_letters[*letter as usize - 'a' as usize] += 1; 
        }
        let mut flag = true;
        for i in 0..s1_letters.len() {
            if substring_letters[i] != s1_letters[i] {
               flag = false;
            }
        }

        if flag {
            return flag;
        }
        start += 1;
        end += 1;
    }

    false
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_inclusion() {
        let s1 = String::from("ab");
        let s2 = String::from("eidbaooo");
        assert!(check_inclusion(s1, s2));
    }

    #[test]
    fn test_not_inclusion() {
        let s1 = String::from("ab");
        let s2 = String::from("eidboaoo");
        assert!(!check_inclusion(s1, s2));
    }

    #[test]
    fn test_not_inclusion_1() {
        let s1 = String::from("adc");
        let s2 = String::from("dcda");
        assert!(check_inclusion(s1, s2));
    }
}
