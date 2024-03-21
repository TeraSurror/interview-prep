use std::cmp::{max, min};

fn max_profit(prices: Vec<i32>) -> i32 {
    let mut result = 0;
    let mut curr_min = prices[0];

    for i in 1..prices.len() {
        curr_min = min(curr_min, prices[i]);
        result = max(result, prices[i] - curr_min);
    }

    return result;
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_max_profit_1() {
        let prices = vec![7, 1, 5, 3, 6, 4];
        let want = 5;
        let got = max_profit(prices);
        assert_eq!(want, got);
    }

    #[test]
    fn test_max_profit_2() {
        let prices = vec![7, 6, 4, 3, 1];
        let want = 0;
        let got = max_profit(prices);
        assert_eq!(want, got);
    }
}
