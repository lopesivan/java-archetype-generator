package ${package};

import jakarta.servlet.ServletException;
import jakarta.servlet.annotation.WebServlet;
import jakarta.servlet.http.HttpServlet;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;

import java.io.IOException;

@WebServlet(name = "helloServlet", value = "/hello")
public class HelloServlet extends HttpServlet
{
    @Override
    protected void doGet(HttpServletRequest request,
                         HttpServletResponse response)
            throws ServletException, IOException
    {
        response.setContentType("text/plain;charset=UTF-8");
        response.getWriter().println("Hello from Jakarta Servlet!");
    }
}
