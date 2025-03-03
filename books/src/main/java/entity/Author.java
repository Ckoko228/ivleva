package entity;
import jakarta.persistence.*;
import lombok.AllArgsConstructor;
import lombok.Getter;
import lombok.NoArgsConstructor;
import lombok.Setter;
import java.util.List;
@Getter
@Setter
@NoArgsConstructor
@AllArgsConstructor
@Entity
@Table(name = "authors")
public class Author {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;
    @Column(nullable = false, length = 50) //NOT NULL, Максимальная длина 50 символов
    private String firstName;
    @Column(nullable = false, length = 50)
    private String lastName;
    @ManyToMany(mappedBy = "authors")
    private List<Book> books;
}
