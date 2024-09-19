import gradio as gr

# Function to format and display the form data
def display_info(name, website, bio, address, email, service_area):
    return f"Name: {name}\nWebsite: {website}\nBio: {bio}\nAddress: {address}\nEmail: {email}\nArea of Service: {service_area}"


# Create the Gradio interface
with gr.Blocks() as demo:
    gr.Markdown("# MOXI Team (SEO Intelligence Desk)\nUse this form to get your website recommendations for SEO.")
    with gr.Row():  # Arrange inputs and output side by side
        with gr.Column():  # Left column for inputs
            name = gr.Textbox(label="Name")
            website = gr.Textbox(label="Website URL")
            bio = gr.Textbox(label="Bio", lines=3)
            address = gr.Textbox(label="Address")
            email = gr.Textbox(label="Email")
            service_area = gr.Textbox(label="Area of Service")
            submit_btn = gr.Button("Submit")

        with gr.Column():
            with gr.Row():
                with gr.Accordion("Title Tag recommendations", open=False):
                    output_text1 = gr.Textbox(label="Recommendations", lines=5)
            with gr.Row():
                with gr.Accordion("Meta Description recommendations", open=False):
                    output_text2 = gr.Textbox(label="Recommendations", lines=5)
            with gr.Row():
                with gr.Accordion("Headings recommendations", open=False):
                    output_text3 = gr.Textbox(label="Recommendations", lines=5)
            with gr.Row():
                with gr.Accordion("Image Optimization recommendations", open=False):
                    output_text4 = gr.Textbox(label="Recommendations", lines=5)
            with gr.Row():
                with gr.Accordion("Structured Data (Schema Markup) recommendations", open=False):
                    output_text5 = gr.Textbox(label="Recommendations", lines=5)
            with gr.Row():
                with gr.Accordion("Sitemap and Robots.txt recommendations", open=False):
                    output_text6 = gr.Textbox(label="Recommendations", lines=5)

            # with gr.Column():  # Right column for displaying output
            #     output_text1 = gr.TextArea(label="Collected Info1", lines=10)

    # Link the button click to the display function
    submit_btn.click(display_info,
                     inputs=[name, website, bio, address, email, service_area],
                     outputs=output_text1)

    submit_btn.click(display_info,
                     inputs=[name, website, bio, address, email, service_area],
                     outputs=output_text2)

# Launch the Gradio interface
demo.launch()