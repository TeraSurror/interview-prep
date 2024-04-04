fn daily_temperatures(temperatures: Vec<i32>) -> Vec<i32> {
    let mut result = vec![0; temperatures.len()]; 
    let mut stack: Vec<(i32, usize)> = Vec::new();
    
    for (index, num) in temperatures.iter().enumerate() {
        while !stack.is_empty() && stack.last().unwrap().0 < *num {
            let (_, stack_idx) = stack.pop().unwrap();
            result[stack_idx] = (index - stack_idx) as i32;
        }
        stack.push((*num, index));
    }

    result
}

#[cfg(test)]
mod tests {
    use super::daily_temperatures;


    #[test]
    fn test_dailt_temps() {
        let temp = vec![73, 74, 75, 71, 69, 72, 76, 73];
        let want = vec![1, 1, 4, 2, 1, 1, 0, 0];
        let got = daily_temperatures(temp); 
        assert_eq!(got, want);
    }

    #[test]
    fn test_dailt_temps_1() {
        let temp = vec![30, 40, 50, 60];
        let want = vec![1, 1, 1, 0];
        let got = daily_temperatures(temp); 
        assert_eq!(got, want);
    }

    #[test]
    fn test_dailt_temps_2() {
        let temp = vec![30, 60, 90];
        let want = vec![1, 1, 0];
        let got = daily_temperatures(temp); 
        assert_eq!(got, want);
    }
}

