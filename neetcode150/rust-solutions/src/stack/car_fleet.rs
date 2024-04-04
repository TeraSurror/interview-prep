fn car_fleet(target: i32, position: Vec<i32>, speed: Vec<i32>) -> i32 {
    let mut position_speed_pair: Vec<(f64, f64)> = position.iter().map(|x| *x as f64).zip(speed.iter().map(|x| *x as f64)).collect();

    position_speed_pair.sort_by(|a, b| a.0.partial_cmp(&b.0).unwrap());

    let mut stack = vec![];
    for (pos, speed) in position_speed_pair.iter().rev() {
        stack.push((target as f64 - pos) / speed);
        if stack.len() >= 2 && stack.last() <= stack.get(stack.len() - 2) {
            stack.pop();
        }
    }

    stack.len() as i32
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_car_fleet_1() {
        let target = 12;
        let position = vec![10,8,0,5,3];
        let speed = vec![2, 4, 1, 1, 3];
        let want = 3;
        let got = car_fleet(target, position, speed);
        assert_eq!(want, got);
    }

    #[test]
    fn test_car_fleet_2() {
        let target = 10;
        let position = vec![3];
        let speed = vec![3];
        let want = 1;
        let got = car_fleet(target, position, speed);
        assert_eq!(want, got);
    }

    #[test]
    fn test_car_fleet_3() {
        let target = 100;
        let position = vec![0, 2, 4];
        let speed = vec![4, 2, 1];
        let want = 1;
        let got = car_fleet(target, position, speed);
        assert_eq!(want, got);
    }
}
