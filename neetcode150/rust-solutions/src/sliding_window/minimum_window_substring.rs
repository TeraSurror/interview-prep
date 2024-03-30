use std::{cmp::min, collections::HashMap};

fn min_window(s: String, t: String) -> String {
    
    let s: Vec<char> = s.chars().collect();

    if t == String::new() || s.len() < t.len() {
        return String::new();
    }

    let mut count_t: HashMap<char, i32> = HashMap::new();
    let mut window: HashMap<char, i32> = HashMap::new();

    for letter in t.chars() {
        *count_t.entry(letter).or_default() += 1;
    } 

    let mut have = 0;
    let want = count_t.len();

    let mut start = 0;
    let mut res: Vec<i32> = vec![-1, -1];
    let mut res_length = usize::MAX;

    for end in 0..s.len() {
        let c = s[end];
        *window.entry(c).or_default() += 1;

        have += (window.get(&c) == count_t.get(&c)) as usize;
        
        while have == want {
            let window_length = end - start + 1;
            if window_length < res_length {
                res = vec![start as i32, end as i32];
            }
            res_length = min(res_length, window_length);
            *window.get_mut(&s[start]).unwrap() -= 1;

            if window.get(&s[start]) < count_t.get(&s[start]) {
                have -= 1;
            }

            start += 1;
        }
    }

    if res[0] > -1 && res[1] > -1 {
        return s[res[0] as usize..=res[1] as usize].into_iter().collect();
    }

    String::new()
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_min_window() {
        let s = String::from("ADOBECODEBANC");
        let t = String::from("ABC");
        assert_eq!(String::from("BANC"), min_window(s, t));
    }

    #[test]
    fn test_min_window_1() {
        let s = String::from("a");
        let t = String::from("a");
        assert_eq!(String::from("a"), min_window(s, t));
    }

    #[test]
    fn test_min_window_2() {
        let s = String::from("a");
        let t = String::from("aa");
        assert_eq!(String::from(""), min_window(s, t));
    }
}


