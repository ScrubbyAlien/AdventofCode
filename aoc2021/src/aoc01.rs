use std::fs;

fn parse() -> Vec<i32> {
    let filename = "inputs/input01.txt";
    let content = fs::read_to_string(filename).unwrap();
    let content_list: Vec<i32> = content
        .trim()
        .split('\n')
        .map(|l| l.parse::<i32>().unwrap())
        .collect();
    return content_list;
}

pub fn part1() {
    let content_list = parse();

    let mut result: i32 = 0;

    for i in 1..content_list.len() {
        if content_list[i] > content_list[i - 1] {
            result = result + 1;
        }
    }

    println!("2021 01 part 1: {}", result);
}

pub fn part2() {
    let content_list = parse();

    let mut new_list: Vec<i32> = Vec::new();

    for i in 2..content_list.len() {
        new_list.push(content_list[i] + content_list[i - 1] + content_list[i - 2]);
    }

    let mut result: i32 = 0;

    for i in 1..new_list.len() {
        if new_list[i] > new_list[i - 1] {
            result = result + 1;
        }
    }

    println!("2021 01 part 2: {}", result);
}
