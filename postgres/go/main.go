package main

import (
	"fmt"
	"os"

	"gopkg.in/ini.v1"

	"gorm.io/driver/postgres"
	"gorm.io/gorm"
)

type Product struct {
	Upc          string
	Description  string
	Manufacturer string
	Category     string
	SubCategory  string
	ProductSize  string
}

type Tabler interface {
	TableName() string
}

func (Product) TableName() string {
	return "product"
}

func main() {
	cfg, err := ini.Load("pipeline.conf")
	if err != nil {
		fmt.Printf("Fail to read file: %v", err)
		os.Exit(1)
	}

	host := cfg.Section("postgres_config").Key("host").String()
	user := cfg.Section("postgres_config").Key("username").String()
	password := cfg.Section("postgres_config").Key("password").String()
	dbname := cfg.Section("postgres_config").Key("database").String()
	port := cfg.Section("postgres_config").Key("port").String()

	dsn := fmt.Sprintf("host=%s user=%s password=%s dbname=%s port=%s sslmode=disable TimeZone=Asia/Bangkok", host, user, password, dbname, port)
	db, err := gorm.Open(postgres.Open(dsn), &gorm.Config{})
	if err != nil {
		panic("failed to connect database")
	}

	var product Product
	db.First(&product, "1111009477")
	fmt.Println(product)

	var products []Product
	db.Limit(5).Find(&products)
	fmt.Println(products)
}
