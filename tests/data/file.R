require(some stuff)

x <- read_csv("/path/to/a/file.shp")

add_five <- function(x){
   return(x + 5)
}

x <- add_five(x)

write_csv(x "/path/to/my/output.csv")
