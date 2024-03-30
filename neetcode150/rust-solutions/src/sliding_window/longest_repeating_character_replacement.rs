use std::collections::HashMap;

fn character_replacement(s: String, k: i32) -> i32 {
    let letters: Vec<char> = s.chars().collect();
    let mut result = 0;

    let mut start = 0;
    let mut max_count = 0;
    let mut map = HashMap::new();

    for end in 0..letters.len() {
        *map.entry(letters[end]).or_default() += 1;
        max_count = max_count.max(*map.get(&letters[end]).unwrap());

        while (end - start + 1) - max_count > k as usize {
            *map.get_mut(&letters[start]).unwrap() -= 1;
            start += 1;
        }

        result = result.max(end - start + 1);
    } 

    result as i32
}
