use std::collections::HashMap;

/*
Sol
1. If len of strings is not equal, return false
2. convert the first string into a hashmap that contains the count of the characters
3. iterate the second list and subtract the count of the characters in the hashmap.
4. if all the values in the hashmap are 0, return true else false
*/
fn valid_anagrams(s: String, t: String) -> bool {
    if s.len() != t.len() {
        return false;
    }

    let mut map: HashMap<char, i32> = HashMap::new();

    for (s_letter, t_letter) in s.chars().zip(t.chars()) {
        *map.entry(s_letter).or_default() += 1; // or_default inserts the default value and returns a mutable ref.
        *map.entry(t_letter).or_default() -= 1;
    }

    map.into_values().all(|cnt| cnt == 0)
}

#[cfg(test)]
mod test {
    use super::*;

    #[test]
    fn true_test() {
        let s1 = String::from("anagram");
        let s2 = String::from("nagaram");
        assert!(valid_anagrams(s1, s2));
    }

    #[test]
    fn false_test() {
        let s1 = String::from("anagram");
        let s2 = String::from("sadffan");
        assert!(!valid_anagrams(s1, s2));
    }

    #[test]
    fn blank_test() {
        let s1 = String::from("anagram");
        let s2 = String::from("");
        assert!(!valid_anagrams(s1, s2));
    }
}
