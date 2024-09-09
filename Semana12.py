import java.util.ArrayList;
import java.util.HashMap;
import java.util.HashSet;
import java.util.List;
import java.util.Map;
import java.util.Set;

public class Library {
    private Map<String, Book> bookCollection;
    private Set<String> userIds;
    private Map<String, User> userCollection;

    public Library() {
        this.bookCollection = new HashMap<>();
        this.userIds = new HashSet<>();
        this.userCollection = new HashMap<>();
    }

    public void addUser(User user) {
        if (!userIds.contains(user.getId())) {
            userIds.add(user.getId());
            userCollection.put(user.getId(), user);
        } else {
            System.out.println("El ID de usuario ya existe");
        }
    }

    public void addBook(Book book) {
        bookCollection.put(book.getIsbn(), book);
    }

    public void lendBook(String userId, String isbn) {
        if (userIds.contains(userId) && bookCollection.containsKey(isbn)) {
            User user = userCollection.get(userId);
            Book book = bookCollection.get(isbn);
            if (book.isAvailable()) {
                book.setAvailable(false);
                user.addBorrowedBook(book);
                System.out.println("Libro prestado a " + user.getName());
            } else {
                System.out.println("El libro no está disponible");
            }
        } else {
            System.out.println("El usuario o el libro no existen");
        }
    }

    public void returnBook(String isbn) {
        if (bookCollection.containsKey(isbn)) {
            Book book = bookCollection.get(isbn);
            book.setAvailable(true);
            System.out.println("Libro devuelto");
        } else {
            System.out.println("El libro no existe");
        }
    }

    public List<Book> searchCatalog(String query) {
        List<Book> results = new ArrayList<>();
        for (Book book : bookCollection.values()) {
            if (book.getTitle().contains(query) || book.getAuthor().contains(query) || book.getCategory().contains(query)) {
                results.add(book);
            }
        }
        return results;
    }

    public List<Book> listBorrowedBooks(String userId) {
        if (userIds.contains(userId)) {
            User user = userCollection.get(userId);
            return user.getBorrowedBooks();
        } else {
            System.out.println("El usuario no existe");
            return new ArrayList<>();
        }
    }
}
public class Main {
    public static void main(String[] args) {
        Library