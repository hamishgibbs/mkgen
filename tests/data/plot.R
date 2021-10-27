require(some stuff)

x <- read_csv("/path/to/a/file.shp")
y <- read_csv("/path/to/a/file.shp")
z <- read_csv("/path/to/a/file.shp")

plot <- function(x){
   return(x + 5)
}

p1 <- plot(x)
p2 <- plot(y)
p3 <- plot(z)

ggsave(p1, "/path/to/my/p1.png")
ggsave(p2, "/path/to/my/p2.png")
ggsave(p3, "/path/to/my/p3.png")
