fn min_eating_speed(piles: Vec<i32>, h: i32) -> i32 {
    let max_piles = *piles.iter().max().unwrap() as usize;

    let mut start = 1;  
    let mut end = max_piles;  

    let mut k = max_piles;

    while start <= end {
        let m = start + (end - start) / 2;
        let hrs: usize = piles.iter().map(|&num_bananas| ((num_bananas - 1) as usize / m) + 1).sum();

        match hrs.cmp(&(h as usize)) {
            std::cmp::Ordering::Less | std::cmp::Ordering::Equal => {
                k = k.min(m);
                end = m - 1;
            },
            std::cmp::Ordering::Greater => start = m + 1,
        }
    }

    k as i32
}

#[cfg(test)]
mod tests {
    use super::min_eating_speed;


    #[test]
    fn test_koko_bananas_1() {
        let piles = vec![3, 6, 7, 11];
        let h = 8;
        let want = 4;
        let got = min_eating_speed(piles, h);

        assert_eq!(want, got);
    }

    #[test]
    fn test_koko_bananas_2() {
        let piles = vec![30, 11, 23, 4, 20];
        let h = 5;
        let want = 30;
        let got = min_eating_speed(piles, h);

        assert_eq!(want, got);
    }

    #[test]
    fn test_koko_bananas_3() {
        let piles = vec![30, 11, 23, 4, 20];
        let h = 6;
        let want = 23;
        let got = min_eating_speed(piles, h);

        assert_eq!(want, got);
    }
}
