use std::collections::HashMap;

/*

1. convert each word to a vector that contains the frequency of each letter
2. insert the letter in a hash map
3. if the vector is already in the hashmap, append the word to the list corresponding to the hash map key
4. return all values of the hashmap

*/
fn group_anagrams(strs: Vec<String>) -> Vec<Vec<String>> {
    let mut map: HashMap<[u8; 26], Vec<String>> = HashMap::new();

    for word in strs {
        let mut key = [0_u8; 26];

        for c in word.chars() {
            key[c as usize - 'a' as usize] += 1;
        }

        if let Some(vals) = map.get_mut(&key) {
            vals.push(word);
        } else {
            map.insert(key, vec![word]);
        }
    }

    map.into_values().collect()
}
