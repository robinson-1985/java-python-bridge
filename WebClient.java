import java.net.URI;
import java.net.http.HttpClient;
import java.net.http.HttpRequest;
import java.net.http.HttpResponse;
import java.net.URLEncoder;
import java.nio.charset.StandardCharsets;

public class WebClient {
    public static void main(String[] args) throws Exception {
        String texto = "Este projeto está ficando sensacional!";
        
        String urlTexto = URLEncoder.encode(texto, StandardCharsets.UTF_8);
        String url = "http://127.0.0.1:8000/analyze?text=" + urlTexto;

        HttpClient client = HttpClient.newHttpClient();
        HttpRequest request = HttpRequest.newBuilder()
                .uri(URI.create(url))
                .GET()
                .build();

        System.out.println("JAVA: Enviando requisição para a API Python...");
        
        HttpResponse<String> response = client.send(request, HttpResponse.BodyHandlers.ofString());

        System.out.println("JAVA: Resposta da API recebida:");
        System.out.println(response.body());
    }
}
