extern crate reqwest;
extern crate scraper;
use std::iter::zip;
use std::error::Error;
use std::io;
use std::process;
use reqwest::Body;
use scraper::{Html, Selector};
use fltk::{
    app, enums,
    prelude::{GroupExt, WidgetExt},
    window,
};


use csv::Writer;
use serde::Serialize;
    
fn TypeOf<T>(_: &T) {
    println!("{}", std::any::type_name::<T>())
}
fn example() -> Result<(), Box<dyn Error>> {
    let mut wtr =  Writer::from_path("crypto.csv")?;
    wtr.write_record(&["Name", "Price", "24H Change", "24H Volume", "Market Cap"])?;

    wtr.flush()?;
    Ok(())
}

fn main() -> Result<(), Box<dyn Error>> {
    
    let response = reqwest::blocking::get(
        "https://crypto.com/price",
    )
    .unwrap()
    .text()
    .unwrap();

    let document = scraper::Html::parse_document(&response);

    let title_selector = scraper::Selector::parse("div.css-ttxvk0>p").unwrap();
    let price_selector = scraper::Selector::parse("div.css-16q9pr7>div").unwrap();
    let change_selector = scraper::Selector::parse("div.css-16q9pr7>p").unwrap();
    let volume_selector = scraper::Selector::parse("table>tbody>tr td:nth-of-type(6)").unwrap();
    let mcap_selector = scraper::Selector::parse("table>tbody>tr td:nth-of-type(7)").unwrap();

    

    let titles= document.select(&title_selector).map(|x| x.inner_html());
    let price = document.select(&price_selector).map(|x| x.inner_html());
    let change = document.select(&change_selector).map(|x| x.inner_html());
    let volume = document.select(&volume_selector).map(|x| x.inner_html());
    let mcap = document.select(&mcap_selector).map(|x| x.inner_html());

    let mut titles_array:Vec<String> = Vec::with_capacity(50);
    let mut price_array:Vec<String> = Vec::with_capacity(50);
    let mut change_array:Vec<String> = Vec::with_capacity(50);
    let mut volume_array:Vec<String> = Vec::with_capacity(50);
    let mut mcap_array:Vec<String> = Vec::with_capacity(50);

  
    titles
    .zip(1..51)
    .for_each(|(item,_)| titles_array.push(item ));
    price
    .zip(1..51)
    .for_each(|(item, _)| price_array.push(item));
    change
    .zip(1..51)
    .for_each(|(item,_)| change_array.push(item ));
    volume
    .zip(1..51)
    .for_each(|(item,_)| volume_array.push(item ));
    mcap
    .zip(1..51)
    .for_each(|(item,_)| mcap_array.push(item ));
    
    
    TypeOf(&titles_array);
    println!("{:?}", titles_array[0]);

    let lent= titles_array.len();
    println!("{}", lent);
    let mut n= 0;
    
    
    
    let mut wtr =  Writer::from_path("crypto.csv")?;
    wtr.write_record(&["Name", "Price", "24H Change", "24H Volume", "Market Cap"])?;
    while n < lent {
        wtr.write_record(&[&titles_array[n],&price_array[n],&change_array[n],&volume_array[n],&mcap_array[n]])?;
        n += 1;
    }
    wtr.flush()?;
    Ok(())
    
    // #[derive(Serialize)]
    // struct Row<'a> {
    //     Name: &'a str,
    // }
    
    // fn example() -> Result<(), Box<dyn Error>> {
    //     let mut wtr = Writer::from_path("crypto.csv");
    //     wtr.serialize(Row  {
    //         Name: "abc",
    //     })?

}
