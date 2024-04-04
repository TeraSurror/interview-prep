fn largest_rectangle_area(mut heights: Vec<i32>) -> i32 {
    let mut stack: Vec<usize> = Vec::new();
    let mut result = 0;
    heights.push(0);
    heights.insert(0, 0);

    for (i, h) in heights.iter().enumerate() {
        while stack.len() > 0 && heights[*stack.last().unwrap()] > *h {
            let j = stack.pop().unwrap();
            let width = (i - stack[stack.len() - 1] - 1) as i32;
            let size = width * heights[j];
            result = result.max(size);
        }
        stack.push(i);
    }

    result
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_largest_area_1() {
        let heights = vec![2,1,5,6,2,3];
        let want = 10;
        let got = largest_rectangle_area(heights);
        assert_eq!(got, want);
    }

    #[test]
    fn test_largest_area_2() {
        let heights = vec![2,4];
        let want = 4;
        let got = largest_rectangle_area(heights);
        assert_eq!(got, want);
    }
}
