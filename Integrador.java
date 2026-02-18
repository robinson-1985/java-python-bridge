import java.io.BufferedReader;
import java.io.InputStreamReader;

public class Integrador {
    public static void main(String[] args) {
        try {
            System.out.println("JAVA: Iniciando integração...");
            
            // O comando que seria digitado no terminal do Ubuntu
            String mensagemParaPython = "ola do java";
            ProcessBuilder pb = new ProcessBuilder("python3", "script.py", mensagemParaPython);
            
            // Inicia o processo
            Process processo = pb.start();
            
            // Lê o que o Python imprimiu no terminal
            BufferedReader leitor = new BufferedReader(new InputStreamReader(processo.getInputStream()));
            String linha;
            
            System.out.println("JAVA: Esperando resposta do Python...");
            while ((linha = leitor.readLine()) != null) {
                System.out.println("-> Resposta capturada: " + linha);
            }

            processo.waitFor(); // Espera o Python terminar
            System.out.println("JAVA: Processo finalizado com sucesso!");

        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
